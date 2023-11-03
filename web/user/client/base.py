# user/client/base.py

class ClientBase:
    def __init__(self, username, email, customer_info):
        self.username = username
        self.email = email
        self.customer_info = customer_info

    def get_order_history(self):
        # Delegate to the OrderHistory class to retrieve order history
        order_history = OrderHistory(self.username, self.email, self.customer_info)
        return order_history.get_order_history()

    def track_order(self, order_id):
        # Delegate to the TrackingOrders class to track the order
        tracking_orders = TrackingOrders(self.username, self.email, self.customer_info)
        return tracking_orders.track_order(order_id)

    def get_favorite_items(self):
        # Delegate to the FavoriteItems class to retrieve favorite items
        favorite_items = FavoriteItems(self.username, self.email, self.customer_info)
        return favorite_items.get_favorite_items()

    def update_profile_info(self, new_info):
        # Delegate to the ProfileInformation class to update profile information
        profile_info = ProfileInformation(self.username, self.email, self.customer_info)
        return profile_info.update_profile_info(new_info)
