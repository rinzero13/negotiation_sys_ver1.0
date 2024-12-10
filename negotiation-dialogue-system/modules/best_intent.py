import random

class IntentManager:
    def __init__(self):
        self.best_intent = "agree"
        self.intent_weights = {}
    
    def intent_weight(self,dialogue_phase):
        # 各段階における意図とその重みの設定
        if dialogue_phase == "initial":
            self.intent_weights = {"counter": 1.0}
        elif dialogue_phase == "negotiating":
            self.intent_weights = {"counter": 0.8, "agree": 0.1, "disagree": 0.1}
        elif dialogue_phase == "finalizing":
            self.intent_weights = {"agree": 0.5, "disagree": 0.5}
        else:
            self.intent_weights = {"agree": 1.0}  # 合意段階ではほぼ「agree」
            
    def select_intent(self, intent):
        #意図を確率的に決定
        total_weight = sum(self.intent_weights.values())
        rand_value = random.uniform(0, total_weight)
        cumulative_weight = 0.0
        
        for intent, weight in self.intent_weights.items():
            cumulative_weight += weight
            if rand_value <= cumulative_weight:
                return intent
        return list(self.intent_weights.keys())[0]  # 最後の意図を返す
        
        
        
        
        
        










        