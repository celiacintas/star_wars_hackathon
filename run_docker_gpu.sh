#!/bin/bash
# -*- ENCODING: UTF-8 -*-

nvidia-docker run -t -i -p 8000:8888 --rm -v $(pwd):/star_wars_hackathon pablo1n7/tatooine:3.4
