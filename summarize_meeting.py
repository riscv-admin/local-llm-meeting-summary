# Copyright (C) 2025 - RISC-V International

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Initial contributor: Rafael Sene <rafael@riscv.org>


import argparse
import os
import sys

# Check if Ollama is installed
try:
    import ollama
except ModuleNotFoundError:
    print("\n🚨 Error: 'ollama' module not found. Please install it using:\n")
    print("    pip install ollama\n")
    sys.exit(1)

def summarize_meeting(file_path, model="mistral"):
    """Reads the meeting minutes from a file and generates a summary using a local LLM model."""
    try:
        # Read the input file
        with open(file_path, "r", encoding="utf-8") as file:
            meeting_text = file.read()

        if not meeting_text.strip():
            print("\n⚠️ Warning: The input file is empty. Please provide valid meeting minutes.\n")
            return None

    except FileNotFoundError:
        print(f"\n🚨 Error: The file '{file_path}' was not found. Please check the file path and try again.\n")
        return None
    except PermissionError:
        print(f"\n🚨 Error: Permission denied when accessing '{file_path}'. Check your file permissions.\n")
        return None

    # Construct the prompt
    prompt = f"""
    Here are the meeting minutes:

    {meeting_text}

    "Summarize the meeting, focusing on:

    * The main discussion points.
    * All decisions made.
    * Action items, including who is responsible and deadlines.
    * Any required follow-up.

    Please present the action items in a clear, bulleted list with responsible parties and deadlines clearly noted."
    """

    try:
        # Generate response using the local LLM model
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])

        if "message" in response and "content" in response["message"]:
            summary = response["message"]["content"]
        else:
            print("\n🚨 Error: Unexpected response format from the model.\n")
            return None

    except ollama.OllamaError as e:
        print(f"\n🚨 Ollama Error: {e}\n")
        return None
    except Exception as e:
        print(f"\n🚨 Unexpected error: {e}\n")
        return None

    # Save summary to a file
    output_file = os.path.splitext(file_path)[0] + "_summary.txt"
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(summary)

    # Print summary to the screen
    print("\n--- Meeting Summary ---\n")
    print(summary)
    print(f"\n✅ Summary saved to: {output_file}")

    return output_file

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Summarize meeting minutes using a local LLM model via Ollama.")
        parser.add_argument("file", help="Path to the meeting minutes file.")
        parser.add_argument("--model", default="mistral", help="Ollama LLM model to use (default: mistral)")

        args = parser.parse_args()
        summarize_meeting(args.file, args.model)

    except KeyboardInterrupt:
        print("\n\n⚠️ Process interrupted by user (Ctrl + C). Exiting gracefully...\n")
        sys.exit(0)
