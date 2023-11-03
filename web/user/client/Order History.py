# user/client/order_history.py
from client import c
from web.user.client.base import ClientBasClientBase

class OrderHistory(ClientBase):
    def __init__(self, username, email, customer_info):
        super().__init__(username, email, customer_info)
        # Initialize any necessary data or connections here

    def get_order_history(self):
        # Method to retrieve the order history
        # You can query the database for order data
        # Return a list of orders (each order could be a dictionary or object)

    def get_order_date_time(self, order):
        # Method to extract the order date and time from an order
        return order["order_date_time"]

    def get_order_number(self, order):
        # Method to extract the order number or ID from an order
        return order["order_number"]

    def get_product_details(self, order):
        # Method to extract product/service details from an order
        return order["product_details"]

    def get_order_status(self, order):
        # Method to extract the order status from an order
        return order["order_status"]

    def get_total_price(self, order):
        # Method to extract the total price from an order
        return order["total_price"]

    def get_shipping_info(self, order):
        # Method to extract shipping information from an order
        return order["shipping_info"]

    def get_order_notes(self, order):
        # Method to extract order notes from an order
        return order["order_notes"]

    def get_action_buttons(self, order):
        # Method to generate action buttons or links for an order
        return {
            "view_details": f"/order/{order['order_number']}",
            "reorder": f"/reorder/{order['order_number']}",
            "track_order": f"/track/{order['tracking_number']}"
        }

    # Add other methods related to order history
