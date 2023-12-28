class InvalidPairError(Exception):
    def __init__(self, message, errors):            
        super().__init__(message)

        self.errors = errors

class UnclosedBlockError(Exception):
    def __init__(self, message, errors):            
        super().__init__(message)

        self.errors = errors

class Parser():
    def __init__(self, script: str):
        self.script = script
    
    def Parse(self) -> str:
        lines = self.script.splitlines()

        inside_block = False

        for line_number, line in enumerate(lines, start=1):
            line = line.strip()

            if not line: continue

            if '{' in line:
                inside_block = True
                continue

            if '}' in line:
                inside_block = False
                continue

            if inside_block and ":" in line:
                parts = line.split(":")

                if len(parts) == 2:
                    property_name = parts[0].strip()
                    property_value = parts[1].strip()

                    if not property_name and property_value:
                        raise InvalidPairError(f"Line {line_number}: Invalid property-value pair: '{line}'", "InvalidPairError")
                    
        if inside_block:
            raise UnclosedBlockError("Error: Unclosed block.")
        
        return True