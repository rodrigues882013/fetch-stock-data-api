defmodule FetchStockDataApiWeb.ApiController do
  use FetchStockDataApiWeb, :controller

  def healthcheck(conn, _params) do
    result = "WORKING"
    send_resp(conn, 200, result)
  end
end
