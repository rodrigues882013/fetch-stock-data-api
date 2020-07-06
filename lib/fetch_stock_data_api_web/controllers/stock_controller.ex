defmodule FetchStockDataApiWeb.StockController do
  use FetchStockDataApiWeb, :controller

  require Logger

  defp fetch_stock_data(%{stock_id: stock_id, start_date: start_date, end_date: end_date}) do
    %{stock_id: stock_id, start_date: start_date, end_date: end_date}
      |> StockFetcher.fetch_data()
  end
end
