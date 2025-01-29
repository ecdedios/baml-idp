from baml_client.sync_client import b
from baml_client.types import Resume
import sys

def example(raw_resume: str) -> Resume: 
    # BAML's internal parser guarantees ExtractResume
    # to be always return a Resume type
    response = b.ExtractResume(raw_resume)
    return response

def example_stream(raw_resume: str) -> Resume:
    stream = b.stream.ExtractResume(raw_resume)
    for msg in stream:
        print(msg) # This will be a PartialResume type
  
    # This will be a Resume type
    final = stream.get_final_response()
    return final

def main():
    """Main entry point of the script."""
    resume_text = """
        Vaibhav Gupta
        vbv@boundaryml.com

        Experience:
        - Founder at BoundaryML
        - CV Engineer at Google
        - CV Engineer at Microsoft

        Skills:
        - Rust
        - C++
    """

    print(example(resume_text))

if __name__ == '__main__':
    sys.exit(main())










__author__ = "Ednalyn C. De Dios, et al."
__copyright__ = "Copyright 2025, IDP with BAML"
__credits__ = ["Boundary"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Ednalyn C. De Dios"
__email__ = "ednalyn.dedios@gmail.com"
__status__ = "Prototype"