defmodule FetchStockDataApi.StockFetcher do
  alias FetchStockDataApi.Stock
  alias FetchStockDataApi.External.http.YahooFinances

  def fetch_data({:error, _msg} = response), do: response

  def fetch_data({:argument_error, _msg} = response), do: response

  def fetch_data(%{stock_id: _, start_date: start_date, end_date: end_date}) do
    params
    |> YahooFinance.fetch_stock_info()
  end

  def fetch_stock_data() do

  end

  defp to_time_stamp(date) do

  end

end
