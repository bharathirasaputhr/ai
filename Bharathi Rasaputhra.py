{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
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
      "source": [
        "***Install the owlready2 module***"
      ],
      "metadata": {
        "id": "8XNhhIAVqdT_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install owlready2"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "UErKx5FJjggu",
        "outputId": "7c98014d-bb87-4890-9149-664e1b96362c"
      },
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting owlready2\n",
            "  Downloading owlready2-0.47.tar.gz (27.3 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m27.3/27.3 MB\u001b[0m \u001b[31m53.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h  Installing build dependencies ... \u001b[?25l\u001b[?25hdone\n",
            "  Getting requirements to build wheel ... \u001b[?25l\u001b[?25hdone\n",
            "  Preparing metadata (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "Building wheels for collected packages: owlready2\n",
            "  Building wheel for owlready2 (pyproject.toml) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for owlready2: filename=owlready2-0.47-cp310-cp310-linux_x86_64.whl size=24075200 sha256=1b5194f2a6dd78839d42bf9a6b9ee200ecb87322be74a640ed000e195598f9ce\n",
            "  Stored in directory: /root/.cache/pip/wheels/27/3e/ba/4171c4b10bba9fe1774fbf8fcf794de889e636ce64ad83a533\n",
            "Successfully built owlready2\n",
            "Installing collected packages: owlready2\n",
            "Successfully installed owlready2-0.47\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Import necessary classes from owlready2**"
      ],
      "metadata": {
        "id": "VBplaZW3qaxW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from owlready2 import get_ontology, Thing, DataProperty"
      ],
      "metadata": {
        "id": "EOFZjMQTjMuD"
      },
      "execution_count": 17,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Load the Ontology**"
      ],
      "metadata": {
        "id": "LJv2oWN_qXg2"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "ontology_path = \"/content/MathTutoringSystem.rdf\"  # Replace with your ontology file path\n",
        "onto = get_ontology(ontology_path).load()\n",
        "print(\"Ontology loaded successfully!\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zjCBAh29j7Sp",
        "outputId": "f8f4df97-cf5c-4582-8d4a-0bb90445b0ec"
      },
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ontology loaded successfully!\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Define Classes and Properties Dynamically**"
      ],
      "metadata": {
        "id": "ffTx_M8SqVFD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "with onto:\n",
        "    # Define the Shape hierarchy\n",
        "    class Shape(Thing):\n",
        "        pass\n",
        "\n",
        "    class Square(Shape):\n",
        "        pass\n",
        "\n",
        "    class Triangle(Shape):\n",
        "        pass\n",
        "\n",
        "    class Circle(Shape):\n",
        "        pass\n",
        "\n",
        "    class Rectangle(Shape):\n",
        "        pass\n",
        "\n",
        "    # Define data properties (attributes for each shape)\n",
        "    class has_side(DataProperty):\n",
        "        range = [float]  # Property for Square\n",
        "\n",
        "    class has_base(DataProperty):\n",
        "        range = [float]  # Property for Triangle\n",
        "\n",
        "    class has_height(DataProperty):\n",
        "        range = [float]  # Property for Triangle\n",
        "\n",
        "    class has_radius(DataProperty):\n",
        "        range = [float]  # Property for Circle\n",
        "\n",
        "    class has_length(DataProperty):\n",
        "        range = [float]  # Property for Rectangle\n",
        "\n",
        "    class has_width(DataProperty):\n",
        "        range = [float]  # Property for Rectangle\n",
        "\n",
        "onto.save(file=\"Updated_MathTutoringSystem.owl\", format=\"rdfxml\")\n",
        "print(\"Ontology updated with necessary classes and properties.\\n\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "hZk7IQI2kBdQ",
        "outputId": "d8392c42-f643-4dad-f6ea-e361e6585339"
      },
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Ontology updated with necessary classes and properties.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **ITS Logic for Area Calculation**"
      ],
      "metadata": {
        "id": "yYtbMoGrqRUP"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def main_menu():\n",
        "    print(\"\\nWelcome to the Intelligent Tutoring System!\")\n",
        "    print(\"Choose a shape to calculate its area:\")\n",
        "    print(\"1. Square\")\n",
        "    print(\"2. Triangle\")\n",
        "    print(\"3. Circle\")\n",
        "    print(\"4. Rectangle\")\n",
        "    print(\"5. Exit\")\n",
        "\n",
        "def calculate_area():\n",
        "    while True:\n",
        "        main_menu()\n",
        "        choice = input(\"Enter your choice (1-5): \")\n",
        "\n",
        "        if choice == \"1\":  # Square\n",
        "            side = float(input(\"Enter the side length of the square: \"))\n",
        "            square = onto.Square(f\"square_{side}\")\n",
        "            square.has_side.append(side)\n",
        "            area = side * side\n",
        "            print(f\"The area of the square is: {area:.2f}\")\n",
        "\n",
        "        elif choice == \"2\":  # Triangle\n",
        "            base = float(input(\"Enter the base of the triangle: \"))\n",
        "            height = float(input(\"Enter the height of the triangle: \"))\n",
        "            triangle = onto.Triangle(f\"triangle_{base}_{height}\")\n",
        "            triangle.has_base.append(base)\n",
        "            triangle.has_height.append(height)\n",
        "            area = 0.5 * base * height\n",
        "            print(f\"The area of the triangle is: {area:.2f}\")\n",
        "\n",
        "        elif choice == \"3\":  # Circle\n",
        "            radius = float(input(\"Enter the radius of the circle: \"))\n",
        "            circle = onto.Circle(f\"circle_{radius}\")\n",
        "            circle.has_radius.append(radius)\n",
        "            area = 3.14159 * radius * radius\n",
        "            print(f\"The area of the circle is: {area:.2f}\")\n",
        "\n",
        "        elif choice == \"4\":  # Rectangle\n",
        "            length = float(input(\"Enter the length of the rectangle: \"))\n",
        "            width = float(input(\"Enter the width of the rectangle: \"))\n",
        "            rectangle = onto.Rectangle(f\"rectangle_{length}_{width}\")\n",
        "            rectangle.has_length.append(length)\n",
        "            rectangle.has_width.append(width)\n",
        "            area = length * width\n",
        "            print(f\"The area of the rectangle is: {area:.2f}\")\n",
        "\n",
        "        elif choice == \"5\":  # Exit\n",
        "            print(\"Thank you for using the Intelligent Tutoring System. Goodbye!\")\n",
        "            break\n",
        "\n",
        "        else:\n",
        "            print(\"Invalid choice. Please try again.\")\n",
        "\n",
        "    # Save instances back to the ontology\n",
        "    onto.save(file=\"Updated_MathTutoringSystem.owl\", format=\"rdfxml\")\n",
        "    print(\"Ontology updated with new instances.\\n\")"
      ],
      "metadata": {
        "id": "OaP7hfskkHFe"
      },
      "execution_count": 20,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Run the ITS**"
      ],
      "metadata": {
        "id": "G8uWkxN4qNtw"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "if __name__ == \"__main__\":\n",
        "    calculate_area()\n",
        "\n",
        "    # Print created instances for verification\n",
        "    print(\"\\nInstances in Updated Ontology:\")\n",
        "    for individual in onto.individuals():\n",
        "        print(f\"- {individual}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "7IiQfTwzkLx5",
        "outputId": "12067b9e-fb03-4679-8968-a0ad41fd4031"
      },
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "Welcome to the Intelligent Tutoring System!\n",
            "Choose a shape to calculate its area:\n",
            "1. Square\n",
            "2. Triangle\n",
            "3. Circle\n",
            "4. Rectangle\n",
            "5. Exit\n",
            "Enter your choice (1-5): 1\n",
            "Enter the side length of the square: 5\n",
            "The area of the square is: 25.00\n",
            "\n",
            "Welcome to the Intelligent Tutoring System!\n",
            "Choose a shape to calculate its area:\n",
            "1. Square\n",
            "2. Triangle\n",
            "3. Circle\n",
            "4. Rectangle\n",
            "5. Exit\n",
            "Enter your choice (1-5): 2\n",
            "Enter the base of the triangle: 6\n",
            "Enter the height of the triangle: 9\n",
            "The area of the triangle is: 27.00\n",
            "\n",
            "Welcome to the Intelligent Tutoring System!\n",
            "Choose a shape to calculate its area:\n",
            "1. Square\n",
            "2. Triangle\n",
            "3. Circle\n",
            "4. Rectangle\n",
            "5. Exit\n",
            "Enter your choice (1-5): 3\n",
            "Enter the radius of the circle: 10\n",
            "The area of the circle is: 314.16\n",
            "\n",
            "Welcome to the Intelligent Tutoring System!\n",
            "Choose a shape to calculate its area:\n",
            "1. Square\n",
            "2. Triangle\n",
            "3. Circle\n",
            "4. Rectangle\n",
            "5. Exit\n",
            "Enter your choice (1-5): 5\n",
            "Thank you for using the Intelligent Tutoring System. Goodbye!\n",
            "Ontology updated with new instances.\n",
            "\n",
            "\n",
            "Instances in Updated Ontology:\n",
            "- MathTutoringSystem.Student1\n",
            "- MathTutoringSystem.square_5.0\n",
            "- MathTutoringSystem.triangle_6.0_9.0\n",
            "- MathTutoringSystem.circle_10.0\n"
          ]
        }
      ]
    }
  ]
}