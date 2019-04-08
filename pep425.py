"""
 Testing wheel stuff
"""
from pip._internal import pep425tags
from pip._internal.cache import WheelCache  # noqa: F401
from pip._internal.wheel import Wheel


_wn="https://files.pythonhosted.org/packages/d4/29/6b4f1e02417c3a1ccc85380f093556ffd0b35dc354078074c5195c8447f2/tensorflow-1.13.1-cp37-cp37m-manylinux1_x86_64.whl#sha256=c41862c65628261229db22e33f9e570d845eeb5cea66dcbaebe404405edaa69b"
wn="tensorflow-1.13.1-cp37-cp37m-manylinux1_x86_64.whl"

w = Wheel(wn)

print(w.file_tags)

tags = pep425tags.get_supported()

print(tags)

inters = set(w.file_tags).intersection(tags)
print(inters)
#            tags = pep425tags.get_supported()
#                    python_tag = pep425tags.implementation_tag

"""
from pip install -v tensorflow

    Skipping link https://files.pythonhosted.org/packages/be/80/18adfb46ba0a4044e9feaa0897ceae4673ac07d34deeb74490bc0d4e4987/tensorflow-1.13.0rc1-cp37-cp37m-manylinux1_x86_64.whl#sha256=d62f8ae5e6693e2e0b34d2d9856030fd541d97ae931bb198684c2d1e753e0823 (from https://pypi.org/simple/tensorflow/); it is not compatible with this Python
    Skipping link https://files.pythonhosted.org/packages/74/1b/8b39fbe2fc8a7f6c9e19824b45b8a295526da466f75e7c53e00c51105664/tensorflow-1.13.0rc2-cp37-cp37m-manylinux1_x86_64.whl#sha256=44ad6e4a094cdb2d59c41a5a49659a1762c36366c397921254885691db3514af (from https://pypi.org/simple/tensorflow/); it is not compatible with this Python
    Skipping link https://files.pythonhosted.org/packages/d4/29/6b4f1e02417c3a1ccc85380f093556ffd0b35dc354078074c5195c8447f2/tensorflow-1.13.1-cp37-cp37m-manylinux1_x86_64.whl#sha256=c41862c65628261229db22e33f9e570d845eeb5cea66dcbaebe404405edaa69b (from https://pypi.org/simple/tensorflow/); it is not compatible with this Python
    Skipping link https://files.pythonhosted.org/packages/9f/4e/402a4d7f21d03cd640b41376727a9ea2bac5a06d2556c04517878dad0c3d/tensorflow-2.0.0a0-cp37-cp37m-manylinux1_x86_64.whl#sha256=13d0a3cab2c912bdd61a5294ade565dc7d1cac090994d22b058ff5ea7ce2056c (from https://pypi.org/simple/tensorflow/); it is not compatible with this Python
"""
