def before_model_callback(callback_context: CallbackContext, llm_request: LlmRequest) -> Optional[LlmResponse]:
  """
  Executes *before* a request is sent to the LLM.

  Return an 'LlmResponse' object to intercept the call to the LLM.
  The LLM *won't* be called. Instead, the framework will use the
  'LlmResponse' we provide as if it came from the model.

  This is the core mechanism for implementing input guardrails, prompt
  validation, or serving responses from a cache. Here, we force the agent to
  call a function instead of thinking with the LLM.
  """
  # Skip the LLM call and return a custom response telling the agent to
  # execute a specific function.
  print(callback_context.variables)
  print(callback_context.variables.update({
      "csat_rating": 5,
      "csat1_submitted": True,
  }))
  print(callback_context.variables)
  if  llm_request.contents[-1].parts[-1].has_function_response('yes_t'):
    print("a")
    return LlmResponse.from_parts([Part.from_text(text="yo")])
  else:
    print("b")
    return LlmResponse.from_parts([Part.from_function_call(name="yes_t", args={})])
