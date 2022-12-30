# xerparser
# rsrc.py


class RSRC:
    """
    A class to represent a Resource.

    ...

    Attributes
    ----------
    uid: str
        Unique ID [rsrc_id]
    clndr_id:
        Unique ID of Calendar assigned to the resource
    name:
        Resource Name [rsrc_name]
    short_name:
        Resource ID [rsrc_short_name]
    type: str
        Resource Type [rsrc_type]
    """

    def __init__(self, **kwargs) -> None:
        self.uid: str = kwargs["rsrc_id"]
        self.clndr_id: str = kwargs["clndr_id"]
        self.name: str = kwargs["rsrc_name"]
        self.short_name: str = kwargs["rsrc_short_name"]
        self.type: str = kwargs["rsrc_type"]

    def __eq__(self, __o: "RSRC") -> bool:
        return all(
            (
                self.name == __o.name,
                self.short_name == __o.short_name,
                self.type == __o.type,
            )
        )

    def __hash__(self) -> int:
        return hash((self.name, self.short_name, self.type))
