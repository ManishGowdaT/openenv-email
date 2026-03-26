import random
from tasks import TASKS


class EmailEnv:
    def __init__(self):
        self.current_task = None
        self.is_done = False

    def reset(self):
        # randomly pick a task each time
        self.current_task = random.choice(TASKS)
        self.is_done = False

        # return initial state
        return self._get_state()

    def _get_state(self):
        # what the agent sees
        return {
            "email": self.current_task["email"],
            "urgency": self.current_task["urgency"],
            "customer_type": self.current_task["customer_type"],
            "sentiment": self.current_task["sentiment"]
        }

    def step(self, action):
        # if already finished, don't process again
        if self.is_done:
            return self._get_state(), 0.0, True

        correct = self.current_task["correct_action"]
        acceptable = self.current_task.get("acceptable_actions", [])

        reward = 0.0  # default

        # main decision logic
        if action == correct:
            reward = 1.0
        elif action in acceptable:
            reward = 0.6
        else:
            reward = 0.0

        # mark episode complete
        self.is_done = True

        return self._get_state(), reward, self.is_done