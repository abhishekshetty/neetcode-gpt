class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        # Objective function: f(x) = x^2
        # Derivative:         f'(x) = 2x
        # Update rule:        x = x - learning_rate * f'(x)
        # Round final answer to 5 decimal places
        def minimize(val:float, lrt: float) -> float:
            return val - lrt * 2 * (val);
        i = 1;
        val = init;
        while i <= iterations:
            val = minimize(val, learning_rate);
            i+=1;
        return round(val, 5);
        
    
