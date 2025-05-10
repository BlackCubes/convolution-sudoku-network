from enum import StrEnum


class ConvolutionSudokuNetworkEnum(StrEnum):
    """
    A custom Enum class that extends StrEnum.

    This class inherits all functionality from StrEnum, including
    string representation and automatic value conversion to strings.

    Example:
        class Visibility(DispatchEnum):
            OPEN = "Open"
            RESTRICTED = "Restricted"

        assert str(Visibility.OPEN) == "Open"
    """
