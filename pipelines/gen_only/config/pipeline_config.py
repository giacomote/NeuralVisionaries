class PipelineConfig:
    """
    Set some configuration variables for the image generation only pipeline.
    """

    # Folder names must end with a '/' character
    # They can be either absolute paths or relative paths (starting from the repository folder)
    results_dir = 'images_inference/gen_only/'

    generation_prompt = 'A high quality studio photograph of a cat on the Moon, with the United States flag behind his back'