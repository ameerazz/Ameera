{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP7QSamPO0ccAXTWdORyNgn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ameerazz/Ameera/blob/main/ameeratry.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9qQvPC7WonoG",
        "outputId": "4696fc52-1d2e-4ef2-9157-210fb7cdcd8c"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Give a number6\n",
            "6 2 1\n",
            "result:  1.0\n",
            "6 3 3\n",
            "result:  1.5\n",
            "6 4 6\n",
            "result:  2.0\n",
            "6 5 10\n",
            "result:  2.5\n",
            "6 6 15\n",
            "result:  3.0\n",
            "6 7 21\n",
            "result:  3.5\n"
          ]
        }
      ],
      "source": [
        "a = int (input (\"Give a number\"))\n",
        "b,c = 1,0\n",
        "while b<= a:\n",
        "  c = c + b\n",
        "  b = b + 1\n",
        "  print (a, b, c)\n",
        "  print (\"result: \", float (c)/(b-1))"
      ]
    }
  ]
}