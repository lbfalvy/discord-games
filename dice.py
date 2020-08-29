from discord.ext import commands
from random import randint
from typing import Tuple, Union, Type, List

@commands.command()
async def roll(ctx, *args):
    # Decode arguments
    dice = []
    for arg in args:
        # Try to decode as a dice request
        dice_data = what_dice(arg)
        if dice_data is None:
            await ctx.send("I don't understand {}".format(arg))
            return
        else: dice.append(dice_data)

    # Roll dice
    for i in range(len(dice)):
        count = dice[i][0]
        sides = dice[i][1]
        results = []
        for _ in range(count):
            results.append(randint(1, sides))
        dice[i] = (sides, results)

    # Print results
    result_parts = []
    for (sides, numbers) in dice:
        num_strings = map(str, numbers)
        result_part = "d{}: ".format(sides) + ", ".join(num_strings)
        result_parts.append(result_part)
    result = "results: " + "; ".join(result_parts)
    if len(result) > 2000:
        result = "Individual results not displayed."
    await ctx.send(result)

    # Print sum unless we only rolled one die of one type
    if len(dice) > 1 or len(dice[0][1]) > 1:
        total = sum(map(lambda x: sum(x[1]), dice))
        await ctx.send("sum: " + str(total))

def what_dice(name: str) -> Union[ Tuple[int, int], Type[None] ]:
    # d20 for example
    if name.startswith("d"):
        num = name.strip("d")
        try:
            return (1, int(num))
        except ValueError:
            return None
    parts = name.split("d")
    if len(parts) != 2: 
        return None
    try:
        return (int(parts[0]), int(parts[1]))
    except ValueError:
        return None