#!/usr/bin/env python
import uuid
mac=uuid.UUID(int = uuid.getnode()).hex[-12:] 
print ":".join([mac[e:e+2] for e in range(0,11,2)])

