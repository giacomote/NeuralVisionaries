import os

import sys
from pathlib import Path

# Loading local files
PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from pipelines.gen_only.pipeline import GenerationPipe
from pipelines.gen_only.config.pipeline_config import PipelineConfig


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