"""
Expense Sharing APP LLD

You live with 3 other friends.

You: User1 (id: u1)

Flatmates: User2 (u2), User3 (u3), User4 (u4)

---

This month's electricity bill was Rs. 1000.

Now you can just go to the app and add that you paid 1000,

select all the 4 people and then select split equally.

Input: u1 1000 4 u1 u2 u3 u4 EQUAL

For this transaction, everyone owes 250 to User1.

The app should update the balances in each of the profiles accordingly. User2 owes User1: 250 (0+250)

User3 owes User1: 250 (0+250)

User4 owes User1: 250 (0+250)

—--------------------
Now, It is the BBD sale on Flipkart and there is an offer on your card.

You buy a few stuffs for User2 and User3 as they asked you to.

The total amount for each person is different.

Input: u1 1250 2 u2 u3 EXACT 370 880

For this transaction, User2 owes 370 to User1 and User3 owes 880 to User1.

The app should update the balances in each of the profiles accordingly.

User2 owes User1: 620 (250+370)

User3 owes User1: 1130 (250+880)

User4 owes User1: 250 (250+0)
"""   

import copy

users = []

users_map = {
}

def check_user_exist(user_id):
    if user_id not in users:
        return False
    return True

def add_user(user_id):
    
    if check_user_exist(user_id):
        return 
    else :
       
        existing_users = copy.deepcopy(users)
        users_map[user_id] = dict()
        for user in existing_users:
            users_map[user_id][user] = 0
            users_map[user][user_id] = 0
        
        users_map[user_id][user_id] = 0
        
        users.append(user_id)
        return True

def expense_processing(owee,ower ,amount):
    users_map[owee][ower]+=amount
    users_map[ower][owee] -=amount
    
        
   
   
# Util 1
def add_expense(amount: float, payee_id: int, total_users: int, user_ids: list, expense_type: str, expense_values: list):
    if expense_type not in ('EQUAL' , 'EXACT'):
        return "Invlaid data"
    
    if expense_type == 'EQUAL':
        
        if expense_values:
            if len(set(expense_values)) != 1 :
                return "Invlaid data"
        else :
            expense_values  = [float(amount/total_users)]*total_users
    else :
        if sum(expense_values) != amount:
            return "Invlaid data"
        if not expense_values:
            return "Invlaid data"
    
    if len(expense_values) != len(user_ids) :
        return "Invlaid data"
    
    for i in range(len(user_ids)):
        add_user(user_ids[i])
        
    for i in range(len(expense_values)):
        
        expense_processing(owee=payee_id,ower=user_ids[i] ,amount= expense_values[i])



# Util 2
def show_balances(user_id):
   """
   Args:
       user_id: int
   Returns:
      {
           "user_id": {
               "<other_user_id>" : +amount,  # amount of money input user owed by this user
               "<other user id>" : -amount   # amount of money input user owe to this user
           }
       }
   """
   user_id_map = users_map[user_id]
   user_id_map.pop(user_id, None)
   return {
       user_id : user_id_map
   }
   pass
   
   
if __name__ == "__main__":

   add_expense(1000, 1, 4, [1,2,3,4], 'EQUAL', []) # 0 250 250 250
   add_expense(1200, 2, 4, [1,2,3,4], 'EXACT', [200, 300, 200, 500])
   print(show_balances(1)) # {1: {2: 50, 3: 250, 4: 250}}
   add_expense(1400, 3, 4, [1,2,3,4], 'EXACT', [400, 400, 200, 400])
   print(show_balances(1)) # {1: {2: 50, 3: -150, 4: 250}}