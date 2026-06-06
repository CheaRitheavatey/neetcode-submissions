class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sorting the positing from large to small
        new_pos = sorted(zip(position, speed), reverse=True)
        stack = []
        print(new_pos)

        # how long it takes to reach target: t = (target - postition)/speed
        for pos,sp in new_pos:
            time = (target - pos)/sp
            while not stack or time > stack[-1]:
                stack.append(time)
           
        return len(stack)
        