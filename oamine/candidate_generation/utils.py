from pathlib import Path
import json
import os
from transformers import BertModel, BertTokenizer, DataCollatorWithPadding
from typing import Any, List, Optional, Text, Union
import io


def load_input(INPUT_FILE: Path):
  docs = []
  with Path(INPUT_FILE).open("r") as f:
    for line in f:
      docs.append(json.loads(line))
  return docs

def save_output(OUTPUT_FILE: Path, docs: List[str]):
  with OUTPUT_FILE.open("w") as f:
    for doc in docs:
      f.write(json.dumps(doc) + "\n")


class IO:

  @classmethod
  def ensure_dir(cls, dir: Union[str, Path], parents=True, exist_ok=False):
    if not Path(dir).is_dir():
      Path(dir).mkdir(parents=parents, exist_ok=exist_ok)


class JsonL(IO):

  @classmethod
  def load(cls, input_file: Path):
    docs = []
    with Path(input_file).open("r") as f:
      for line in f:
        docs.append(json.loads(line))
    return docs

  @classmethod
  def save(cls, output_file: Union[str, Path], docs: List[Any]):
    output_file = Path(output_file)
    cls.ensure_dir(output_file.parent)
    with output_file.open("w") as f:
      for doc in docs:
        f.write(json.dumps(doc) + "\n")


class ModelUtils:

  @staticmethod
  def _get_default_model_path(model_path: Optional[Text] = None) -> Text:
    return model_path if model_path else os.path.join(os.path.dirname(__file__), "data", "model")

  @staticmethod
  def _is_local(model_path: Optional[Text] = None) -> bool:
    True if not model_path else os.path.exists(model_path)

  @staticmethod
  def load_pretrained_model(model_path: Text = "myedibleenso/oamine", output_hidden_states: bool = True) -> BertModel:
    """Loads a pre-trained BERT model"""
    model_path = ModelUtils._get_default_model_path(model_path)
    is_local = ModelUtils._is_local(model_path)
    return BertModel.from_pretrained(
      model_path, 
      output_hidden_states=output_hidden_states, 
      local_files_only=is_local
    )
  
  @staticmethod
  def load_pretrained_tokenizer(model_path: Text = "myedibleenso/oamine", do_lower_case=True) -> BertTokenizer:
    """Loads a pre-trained tokenizer suitable for use with a BERT-based model"""
    model_path = ModelUtils._get_default_model_path(model_path)
    is_local = ModelUtils._is_local(model_path)
    return BertTokenizer.from_pretrained(
      model_path, 
      do_lower_case=do_lower_case, 
      local_files_only=is_local
    )


class TextIO(IO):

  @classmethod
  def save(cls, output_file: Union[str, Path, io.IOBase], docs: List[str]):
    if isinstance(output_file, io.IOBase):
      f = output_file
      for doc in docs:
        f.write(doc + "\n")
    else:
      output_file = Path(output_file)
      cls.ensure_dir(output_file.parent)
      with output_file.open("w") as f:
        for doc in docs:
          f.write(doc + "\n")

  @classmethod
  def load_lines(cls, fname, use_int=False):
    docs = []
    with open(fname, "r") as f:
      for line in f:
        if use_int:
          docs.append(int(line.strip()))
        else:
          docs.append(line.strip())
    return docs
