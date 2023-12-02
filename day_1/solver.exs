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

string_to_number = %{
  "one" => 1,
  "two" => 2,
  "three" => 3,
  "four" => 4,
  "five" => 5,
  "six" => 6,
  "seven" => 7,
  "eight" => 8,
  "nine" => 9
}

ends_with_number_string = fn str ->
  Enum.reduce(Map.keys(string_to_number), {:not_found, nil}, fn key, acc ->
    if String.ends_with?(str, key) do
      {:found, Map.get(string_to_number, key)}
    else
      acc
    end
  end)
end

result =
  input_data
  |> Enum.reduce(0, fn line, result ->
    {{first, second}, _} =
      line
      |> String.graphemes()
      |> Enum.reduce({{}, ""}, fn ch, {pair, str} ->
        {was_found, value} = ends_with_number_string.(str <> ch)

        cond do
          String.match?(ch, ~r"\d") ->
            as_int = String.to_integer(ch)

            if tuple_size(pair) == 0 do
              {{as_int, as_int}, ""}
            else
              {{elem(pair, 0), as_int}, ""}
            end

          was_found == :found ->
            if tuple_size(pair) == 0 do
              {{value, value}, str <> ch}
            else
              {{elem(pair, 0), value}, str <> ch}
            end

          true ->
            {pair, str <> ch}
        end
      end)

    result + first * 10 + second
  end)

IO.puts("Answer to part 2 = #{result}")
