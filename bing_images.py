from bing_image_downloader import downloader

downloader.download("F-22", limit=1000, output_dir='downloads', adult_filter_off=True, force_replace=False, timeout=60)