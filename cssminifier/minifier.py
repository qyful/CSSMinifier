from .parser import Parser

class InvalidScriptError(Exception):
    def __init__(self, message, errors):            
        super().__init__(message)

        self.errors = errors

class Minifier():
    def __init__(self, script: str):
        parser = Parser(script)

        parsed = parser.Parse()

        if parsed:
            self.parsed_script = script
        else:
            raise InvalidScriptError("Error: The provided script could not be parsed.")

    def __call__(self):
        return self._minify(self.parsed_script)

    def _minify(self, script: str) -> list[str]:
        lines = script.splitlines()

        lines = self._remove_comments(lines)

        minified_lines = []

        for line in lines:
            minified_lines.append(line.strip())

        return "".join(minified_lines)
                                  
    def _remove_comments(self, script: list[str]) -> list[str]:
        cleaned_lines = []
        inside_multiline_comment = False

        for line in script:
            # Check for multiline comments
            if inside_multiline_comment:
                if '*/' in line:
                    inside_multiline_comment = False
                    line = line.split('*/', 1)[1].lstrip()
                continue
            elif '/*' in line:
                inside_multiline_comment = True
                if '*/' in line:
                    inside_multiline_comment = False
                    line = line.split('*/', 1)[1].lstrip()
                continue

            # Remove single-line comments
            if '//' in line:
                line = line.split('//', 1)[0].rstrip()
            cleaned_lines.append(line)

        return cleaned_lines