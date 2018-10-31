# -*- coding: utf-8 -*-
import argparse

from bank_app import create_app

application = create_app()

parser = argparse.ArgumentParser()
parser.add_argument("--port", type=int, default=5000)
parser.add_argument("--host", default="127.0.0.1")
args = parser.parse_args()
application.run(port=args.port, host=args.host)
