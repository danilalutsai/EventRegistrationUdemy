"""Grade book — no imports, pure builtins."""

PASS_MARK = 60
CURVE = 1.05
LABELS = {"A": 90, "B": 80, "C": 70, "D": PASS_MARK}


class Student:
    """One student and their scores."""

    __slots__ = ("name", "scores")

    def __init__(self, name: str, scores: list[int] | None = None) -> None:
        if not name.strip():
            raise ValueError("name must not be blank")
        self.name = name
        self.scores = scores or []

    def __repr__(self) -> str:
        return f"Student({self.name!r}, n={len(self.scores)})"

    def __lt__(self, other: "Student") -> bool:
        return self.average < other.average

    @property
    def average(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)

    @property
    def letter(self) -> str:
        curved = self.average * CURVE
        for letter, floor in LABELS.items():
            if curved >= floor:
                return letter
        return "F"

    def add(self, *marks: int) -> None:
        for mark in marks:
            if not 0 <= mark <= 100:
                raise ValueError(f"mark out of range: {mark}")
            self.scores.append(mark)


class GradeBook:
    def __init__(self) -> None:
        self.students: dict[str, Student] = {}

    def __len__(self) -> int:
        return len(self.students)

    def __getitem__(self, name: str) -> Student:
        try:
            return self.students[name]
        except KeyError:
            raise LookupError(f"no student named {name}") from None

    def enroll(self, name: str) -> Student:
        student = self.students.setdefault(name, Student(name))
        return student

    def passing(self) -> list[Student]:
        return sorted(
            (s for s in self.students.values() if s.average >= PASS_MARK),
            reverse=True,
        )

    def report(self) -> str:
        lines = []
        for student in sorted(self.students.values(), reverse=True):
            bar = "#" * int(student.average // 10)
            lines.append(f"{student.name:<10} {student.average:6.2f} {student.letter}  {bar}")
        return "\n".join(lines)


def simulate(seed: int = 7, count: int = 5) -> GradeBook:
    """Deterministic pseudo-random marks — no random module needed."""
    book = GradeBook()
    state = seed
    for i in range(count):
        student = book.enroll(f"user{i:02d}")
        for _ in range(4):
            state = (state * 1103515245 + 12345) % 2147483648
            student.add(40 + state % 61)
    return book


if __name__ == "__main__":
    gradebook = simulate()
    print(gradebook.report())
    print(f"{len(gradebook.passing())}/{len(gradebook)} passing")

    top, *rest = gradebook.passing()
    match top.letter:
        case "A" | "B":
            print(f"{top.name} leads with {top.letter}")
        case _:
            print("nobody excelled")
