# في الواقع، هذه الخدمة ستتعامل مع قاعدة بيانات
# هنا نستخدم قاموس بسيط للتوضيح

users = {}

class UserService:
    def get_user_info(self, user_id):
        return users.get(user_id)

    def update_user_info(self, user_id, info):
        users[user_id] = info
        return users[user_id]

    def create_user(self, user_id, name):
        if user_id not in users:
            users[user_id] = {'name': name, 'phone': '', 'address': ''}
        return users[user_id]