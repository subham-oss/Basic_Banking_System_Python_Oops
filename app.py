import streamlit as st
from main import Bank


# ---------------------------------
# Page configuration
# ---------------------------------

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)


# ---------------------------------
# Initialize bank
# ---------------------------------

bank = Bank()


# ---------------------------------
# Header
# ---------------------------------

st.title("🏦 Bank Management System")
st.caption("Simple Banking CRUD Application using Python + Streamlit")


# ---------------------------------
# Sidebar
# ---------------------------------

st.sidebar.title("Menu")

menu = st.sidebar.radio(
    "Select Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Account Details",
        "Update Details",
        "Delete Account"
    ]
)


# =========================================================
# CREATE ACCOUNT
# =========================================================

if menu == "Create Account":

    st.header("🧑‍💼 Create New Account")

    with st.form("create_account_form"):

        name = st.text_input("Full Name")

        age = st.number_input(
            "Age",
            min_value=1,
            max_value=120,
            value=18
        )

        email = st.text_input("Email")

        pin = st.text_input(
            "4 Digit PIN",
            type="password",
            max_chars=4
        )

        submitted = st.form_submit_button(
            "Create Account"
        )

        if submitted:

            if not pin.isdigit():
                st.error("PIN must contain only numbers.")

            elif len(pin) != 4:
                st.error("PIN must be exactly 4 digits.")

            else:

                success, result = bank.create_account(
                    name=name,
                    age=age,
                    email=email,
                    pin=int(pin)
                )

                if success:

                    st.success("Account created successfully!")

                    st.info(
                        f"Account Number: **{result['account_number']}**"
                    )

                    st.write(f"**Name:** {result['name']}")
                    st.write(f"**Age:** {result['age']}")
                    st.write(f"**Email:** {result['email']}")
                    st.write(f"**Balance:** ₹{result['balance']:,.2f}")

                    st.warning(
                        "Please save your account number and PIN."
                    )

                else:
                    st.error(result)


# =========================================================
# DEPOSIT
# =========================================================

elif menu == "Deposit Money":

    st.header("💰 Deposit Money")

    with st.form("deposit_form"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            step=100.0
        )

        submitted = st.form_submit_button(
            "Deposit"
        )

        if submitted:

            if not pin.isdigit() or len(pin) != 4:
                st.error("Invalid PIN.")

            else:

                success, message = bank.deposit(
                    account_number,
                    int(pin),
                    amount
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# =========================================================
# WITHDRAW
# =========================================================

elif menu == "Withdraw Money":

    st.header("💸 Withdraw Money")

    with st.form("withdraw_form"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "Amount",
            min_value=1.0,
            step=100.0
        )

        submitted = st.form_submit_button(
            "Withdraw"
        )

        if submitted:

            if not pin.isdigit() or len(pin) != 4:
                st.error("Invalid PIN.")

            else:

                success, message = bank.withdraw(
                    account_number,
                    int(pin),
                    amount
                )

                if success:
                    st.success(message)
                else:
                    st.error(message)


# =========================================================
# ACCOUNT DETAILS
# =========================================================

elif menu == "Account Details":

    st.header("👤 Account Details")

    with st.form("details_form"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        submitted = st.form_submit_button(
            "View Details"
        )

        if submitted:

            if not pin.isdigit() or len(pin) != 4:
                st.error("Invalid PIN.")

            else:

                account = bank.get_details(
                    account_number,
                    int(pin)
                )

                if account is None:

                    st.error(
                        "Invalid account number or PIN."
                    )

                else:

                    st.success("Account found!")

                    col1, col2 = st.columns(2)

                    with col1:
                        st.write("**Account Number**")
                        st.write(account["account_number"])

                        st.write("**Name**")
                        st.write(account["name"])

                        st.write("**Age**")
                        st.write(account["age"])

                    with col2:

                        st.write("**Email**")
                        st.write(account["email"])

                        st.write("**Balance**")
                        st.metric(
                            "Current Balance",
                            f"₹{account['balance']:,.2f}"
                        )


# =========================================================
# UPDATE DETAILS
# =========================================================

elif menu == "Update Details":

    st.header("✏️ Update Account Details")

    account_number = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "Current PIN",
        type="password",
        max_chars=4
    )

    update_type = st.selectbox(
        "What do you want to update?",
        [
            "Name",
            "Email",
            "PIN"
        ]
    )

    if update_type == "Name":

        new_name = st.text_input(
            "New Name"
        )

    elif update_type == "Email":

        new_email = st.text_input(
            "New Email"
        )

    else:

        new_pin = st.text_input(
            "New 4 Digit PIN",
            type="password",
            max_chars=4
        )

    if st.button("Update"):

        if not pin.isdigit() or len(pin) != 4:

            st.error("Invalid current PIN.")

        else:

            if update_type == "Name":

                success, message = bank.update_details(
                    account_number,
                    int(pin),
                    name=new_name
                )

            elif update_type == "Email":

                success, message = bank.update_details(
                    account_number,
                    int(pin),
                    email=new_email
                )

            else:

                if not new_pin.isdigit() or len(new_pin) != 4:

                    st.error(
                        "New PIN must contain exactly 4 digits."
                    )

                    success = False
                    message = ""

                else:

                    success, message = bank.update_details(
                        account_number,
                        int(pin),
                        new_pin=int(new_pin)
                    )

            if success:
                st.success(message)

            elif message:
                st.error(message)


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif menu == "Delete Account":

    st.header("🗑️ Delete Account")

    st.warning(
        "⚠️ Deleting an account is permanent."
    )

    with st.form("delete_form"):

        account_number = st.text_input(
            "Account Number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4
        )

        confirm = st.checkbox(
            "I understand that this account will be permanently deleted."
        )

        submitted = st.form_submit_button(
            "Delete Account"
        )

        if submitted:

            if not confirm:

                st.error(
                    "Please confirm account deletion."
                )

            elif not pin.isdigit() or len(pin) != 4:

                st.error("Invalid PIN.")

            else:

                success, message = bank.delete_account(
                    account_number,
                    int(pin)
                )

                if success:
                    st.success(message)

                else:
                    st.error(message)