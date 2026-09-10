import uuid
from datetime import datetime
from sqlalchemy import Uuid,text,DateTime,func
from sqlalchemy.orm import Mapped, mapped_column

class UUIDStampz:

    id:Mapped[uuid.UUID]=mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        nullable=False,
        default=uuid.uuid4,
        server_default=text("gen_random_uuid()"),
    )

    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        server_default=func.now(),
        nullable=False,
    )