defmodule FetchStockDataApiWeb.Router do
  use FetchStockDataApiWeb, :router

  pipeline :api do
    plug(:accepts, ["json"])
  end

  scope "/api", FetchStockDataApiWeb do
    pipe_through(:api)
    get("/", ApiController, :info)
    get("/healthcheck", ApiController, :healthcheck)
    get("/stock/:stock_id", StockController, )
  end
end
