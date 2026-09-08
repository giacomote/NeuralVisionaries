import torch
from diffusers import StableDiffusion3Pipeline


class GenerationPipe:
    def __init__(self):
            self._model_id = 'stabilityai/stable-diffusion-3.5-large'
            self._inference_pipe = None

    def generate_image(
        self,
        prompt: str,
        output_filename: str = 'result.png',
        device: str = 'cuda'
    ):
        
        print('--- Image Generation Started ---\n')
        
        if self._inference_pipe is None:
            print('[I 1/3] Loading base model for inference...')
            self._inference_pipe = StableDiffusion3Pipeline.from_pretrained(
                self._model_id,
                dtype=torch.bfloat16
            ).to(device)

            # pipe.enable_model_cpu_offload()  # Automatic offloading to GPU (to avoid using only the GPU)
            # pipe.vae.enable_tiling()  # Tiling for VAE decoding (to save VRAM)

        else:
            print('[I 1/3] Reusing cached base model...')

        print(f'[I 2/3] Generating image...')
        image = self._inference_pipe(
            prompt=prompt,
            negative_prompt='blurry, distorted, low quality, bad anatomy',
            num_inference_steps=28,
            guidance_scale=4.5,
            width=1024,
            height=1024
        ).images[0]

        print('[I 3/3] Saving result...')
        image.save(output_filename)
        print(f'[OK] Image saved: {output_filename}')

        print('\n--- Image Generation Ended! ---')