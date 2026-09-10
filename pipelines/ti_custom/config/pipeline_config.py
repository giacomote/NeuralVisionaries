class PipelineConfig:
    """
    Set some configuration variables for the personalization pipeline.
    These are used both during the training and the testing processes.
    """

    # Folder names must end with a '/' character
    # They can be either absolute paths or relative paths (starting from the repository folder)
    data_dir = '/data/'
    adaptation_dir = 'adaptation_inference/'
    results_dir = '/images_inference/ti_custom/'

    placeholder_token = '<sks>'
    class_token = 'backpack'
    
    training_prompt = 'A photo of {0}'
    generation_prompt = 'A high quality studio photograph of {0} on the Moon, with the United States flag behind his back'