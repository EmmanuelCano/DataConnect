# DataConnect
DataConnect API Postman Collection


# Possible Results

# Set a Password that does not match password criteria

{
    "error": {
        "message": "Unable to update Dataconnect password. Invalid Password : Password does not contains at least one special character #$%&*+,-.:;=?^_~. "
    },
    "version": "1.0.0"
}

# Password Updated Successfully 
{
    "success": {
        "message": "Dataconnect password has been updated successfully"
    },
    "version": "1.0.0"
}


# Password Expiry 
{
    "success": {
        "message": "Dataconnect password expiry has been updated successfully as 3  days"
    },
    "version": "1.0.0"
}

# Update Feature Status: Enable

Enable
{
    "error": {
        "message": "Skipping update as dataconnect is already enabled"
    },
    "version": "1.0.0"
}

#  Update Feature Status: Disable
{
    "success": {
        "message": "Dataconnect Setting has been disabled and dataconnect certificate removed from trust store successfully"
    },
    "version": "1.0.0"
}

