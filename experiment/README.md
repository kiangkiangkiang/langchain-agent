# Call the LLM to see what to do.
output = self._action_agent.plan(
    intermediate_steps,
    callbacks=run_manager.get_child() if run_manager else None,
    **inputs,
)


實際運行的 agent (not agentexecutor)
AGENT_TO_CLASS