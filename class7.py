{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyObbNqgaHT4Jw7PQO/I5ixP",
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
        "<a href=\"https://colab.research.google.com/github/Vic24Rich/while_loop-for_and_def/blob/main/class7.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xns_nLGcAOes",
        "outputId": "cbbf707c-a0e5-4538-ff9f-971107c785d5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Este é uma nº aleatório: 5\n"
          ]
        }
      ],
      "source": [
        "# 1 - Crie um número aleatório de 10, 5\n",
        "import random\n",
        "\n",
        "ale = random.randint(5,10)\n",
        "print(f'Este é uma nº aleatório: {ale}')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 2 - Crie 3 números aleatórios\n",
        "import random\n",
        "\n",
        "ale1 = random.randrange(2,4)\n",
        "ale2 = random.randrange(4,8)\n",
        "ale3 = random.randrange(8,12)\n",
        "\n",
        "print(f'Este é o 1º numero aleatório: {ale1}')\n",
        "\n",
        "print(f'Este é o 2º numero aleatório: {ale2}')\n",
        "\n",
        "print(f'Este é o 3º numero aleatório: {ale3}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "M3V946g5AZKX",
        "outputId": "8968ae37-dc3f-46b1-e533-b2af213ee2fd"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Este é o 1º numero aleatório: 2\n",
            "Este é o 2º numero aleatório: 7\n",
            "Este é o 3º numero aleatório: 9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 3 - Crie um número aleatório entre 10 a 30 utilize o range()\n",
        "import random\n",
        "\n",
        "ale4 = random.randrange(10,30)\n",
        "\n",
        "print(f'Este é o 1º numero aleatório: {ale4}')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xDNqCEHHAc2k",
        "outputId": "4e33afeb-de78-46d0-cd6e-923d45e15b02"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Este é o 1º numero aleatório: 18\n"
          ]
        }
      ]
    }
  ]
}
