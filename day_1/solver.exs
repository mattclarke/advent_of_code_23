file = "input.txt"

input_data =
  File.stream!(file)
  |> Stream.map(&String.replace(&1, "\n", ""))
  |> Enum.to_list()

# |> IO.inspect()

result =
  input_data
  |> Enum.reduce(0, fn line, result ->
    {first, second} =
      line
      |> String.graphemes()
      |> Enum.reduce({}, fn ch, acc ->
        cond do
          String.match?(ch, ~r"\d") and tuple_size(acc) == 0 ->
            as_int = String.to_integer(ch)
            {as_int, as_int}

          String.match?(ch, ~r"\d") ->
            {elem(acc, 0), String.to_integer(ch)}

          true ->
            acc
        end
      end)

    result + first * 10 + second
  end)

IO.puts("Answer to part 1 = #{result}")

digit_strings = [
  "one",
  "two",
  "three",
  "four",
  "five",
  "six",
  "seven",
  "eight",
  "nine"
]

starts_with_number_string = fn str ->
  digit_strings
  |> Enum.with_index(1)
  |> Enum.reduce(nil, fn {number, index}, acc ->
    if String.starts_with?(str, number) do
      index
    else
      acc
    end
  end)
end

update_first_last = fn
  current, nil -> current
  {}, value -> {value, value}
  {f, _}, value -> {f, value}
end

result =
  input_data
  |> Enum.reduce(0, fn line, result ->
    {first, second} =
      line
      |> String.graphemes()
      |> Enum.with_index()
      |> Enum.reduce({}, fn {ch, i}, acc ->
        value =
          cond do
            String.match?(ch, ~r"\d") ->
              String.to_integer(ch)

            string_digit = starts_with_number_string.(String.slice(line, i..-1)) ->
              string_digit

            true ->
              nil
          end

        update_first_last.(acc, value)
      end)

    result + first * 10 + second
  end)

IO.puts("Answer to part 2 = #{result}")
