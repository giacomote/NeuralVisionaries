import os

import sys
from pathlib import Path

# Loading local files
PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from pipeline_generation.pipeline import GenerationPipe
from pipeline_generation.config.pipeline_config import PipelineConfig


if __name__ == '__main__':
    os.makedirs(PipelineConfig.results_dir, exist_ok=True)

    subject_id = PipelineConfig.data_dir.split('/')[-1]
    output_file = PipelineConfig.results_dir + str(len(os.listdir(PipelineConfig.results_dir))) + '_' + subject_id + '.png'

    generation_prompt = PipelineConfig.generation_prompt.format(PipelineConfig.class_token)

    pipe = GenerationPipe()
    pipe.generate_personalized_image(
        prompt=generation_prompt,
        output_filename=output_file
    )