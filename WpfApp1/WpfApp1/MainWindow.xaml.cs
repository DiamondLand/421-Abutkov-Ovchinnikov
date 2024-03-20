using System;
using System.Windows;
using System.Windows.Controls;

namespace ShapeAreaCalculator
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void ShapeSelectionChanged(object sender, RoutedEventArgs e)
        {
            if (sender is RadioButton radioButton && radioButton.IsChecked == true)
            {
                string shape = radioButton.Content.ToString();
                HideAllPanels();

                switch (shape)
                {
                    case "Квадрат":
                        squarePanel.Visibility = Visibility.Visible;
                        break;
                    case "Круг":
                        circlePanel.Visibility = Visibility.Visible;
                        break;
                    case "Прямоугольник":
                        rectanglePanel.Visibility = Visibility.Visible;
                        break;
                }
            }
        }

        private void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            double area = 0;
            string shapeName = "";

            if (squareRadioButton.IsChecked == true)
            {
                if (ValidatePositiveNumber(sideTextBox.Text, out double side))
                {
                    area = side * side;
                    shapeName = "квадрата";
                }
                else
                {
                    return;
                }
            }
            else if (circleRadioButton.IsChecked == true)
            {
                if (ValidatePositiveNumber(radiusTextBox.Text, out double radius))
                {
                    area = Math.PI * radius * radius;
                    shapeName = "круга";
                }
                else
                {
                    return;
                }
            }
            else if (rectangleRadioButton.IsChecked == true)
            {
                if (ValidatePositiveNumber(lengthTextBox.Text, out double length) &&
                    ValidatePositiveNumber(widthTextBox.Text, out double width))
                {
                    area = length * width;
                    shapeName = "прямоугольника";
                }
                else
                {
                    return;
                }
            }

            if (area == 0)
            {
                resultTextBlock.Text = "Пожалуйста, выберите фигуру и введите соответствующие данные.";
            }
            else
            {
                resultTextBlock.Text = $"Площадь {shapeName}: {area}";
            }
        }

        private bool ValidatePositiveNumber(string input, out double value)
        {
            if (double.TryParse(input, out value))
            {
                if (value <= 0)
                {
                    resultTextBlock.Text = "Введите положительное значение.";
                    return false;
                }
                return true;
            }
            else
            {
                resultTextBlock.Text = "Введите числовое значение.";
                return false;
            }
        }

        private void HideAllPanels()
        {
            squarePanel.Visibility = Visibility.Collapsed;
            circlePanel.Visibility = Visibility.Collapsed;
            rectanglePanel.Visibility = Visibility.Collapsed;
        }
    }
}
