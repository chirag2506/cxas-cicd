def update_name_email(name: str, email: str, phone: str) -> str:
  if len(phone) != 10:
    return "Failed because phone number is not of 10 digits"
  
  context.variables["user_name"] = name
  context.variables["user_email"] = email
  context.variables["user_phone"] = phone

  if name.lower() == "chirag":
    context.variables["message_to_user"] = "hello, authenticated user"
  else:
    context.variables["message_to_user"] = "i am sorry, but you are unauthenticated"

  return "success"