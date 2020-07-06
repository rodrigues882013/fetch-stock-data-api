defmodule AdInsertionService.External.ShouldIPay do
  require Logger
  use Tesla, only: [request: 2]

  plug Tesla.Middleware.PathParams
  plug(Tesla.Middleware.BaseUrl, Application.get_env(:fetch_stock_data_api, :yahoo_finance_pay_url))
  plug(Tesla.Middleware.JSON)
  plug(Tesla.Middleware.Timeout, timeout: 200)
  @header [{"content-type", "application/json"}]

  def fetch_stock_info(stock_id, start_date, end_date) do
    call
    |> handle_response
    |> send_response(result)
  end

  defp call(stock_id, start_date, end_date) do
    params = [stock_id: stock_id]
    get(
      '/v8/finance/chart/:stock_id',
      opts: [path_param: params],
      query: [
        start_date: start_date,
        end_date: end_date,
        interval: '1d',
        includePrePros: 'prepros',
        events: 'div,splits'])
  end
end
