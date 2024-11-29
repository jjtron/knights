from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

Dual = Symbol("I am both a knight and a knave.")
TwoKnaves = Symbol("We are both knaves.")
SameKind = Symbol("We are the same kind.")
DiffKind = Symbol("We are different kinds.")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Implication(Dual, And(AKnave, Not(AKnight))),
    Dual
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Implication(TwoKnaves, And(AKnave, BKnight)),
    TwoKnaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Implication(SameKind, Or(And(AKnave,BKnave),And(AKnight,BKnight))),
    Implication(DiffKind, Or(And(AKnight,BKnave),And(AKnave,BKnight))),
    Implication(AKnight, BKnight),
    Implication(AKnave, Or(And(AKnight,BKnave),And(BKnight,AKnave))),
    Implication(BKnight, AKnave),
    Implication(BKnave, Or(And(AKnave,BKnave),And(BKnight,AKnight))),
    SameKind, DiffKind
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    '''
    print(model_check(knowledge0, AKnight))
    return
    '''

    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        #("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                #print("knowledge:", knowledge)
                #print("symbol", symbol)
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
