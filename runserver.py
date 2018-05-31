#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

import matplotlib

matplotlib.use('Agg')

from project import app, Configuration

if __name__ == '__main__':
    port = int(os.environ.get("PORT", Configuration.default_port))
    app.run('0.0.0.0', port=port)
