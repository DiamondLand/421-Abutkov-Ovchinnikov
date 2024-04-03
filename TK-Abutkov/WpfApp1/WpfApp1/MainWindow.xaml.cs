using System;
using System.Text.RegularExpressions;
using System.Windows;

namespace ExamScoreCalculator
{
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void CalculateButton_Click(object sender, RoutedEventArgs e)
        {
            try
            {
                int task1Score = ParseAndValidateInput(Task1TextBox.Text, 10);
                int task2Score = ParseAndValidateInput(Task2TextBox.Text, 50);
                int task3Score = ParseAndValidateInput(Task3TextBox.Text, 30);
                int task4Score = ParseAndValidateInput(Task4TextBox.Text, 10);

                int totalScore = task1Score + task2Score + task3Score + task4Score;

                string grade;
                if (totalScore >= 70)
                {
                    grade = "5 (отлично)";
                }
                else if (totalScore >= 40)
                {
                    grade = "4 (хорошо)";
                }
                else if (totalScore >= 20)
                {
                    grade = "3 (удовлетворительно)";
                }
                else
                {
                    grade = "2 (неудовлетворительно)";
                }

                ResultLabel.Content = $"Сумма баллов: {totalScore}\nОценка: {grade}";
            }
            catch (FormatException)
            {
                MessageBox.Show("Пожалуйста, введите числовое значение для каждого задания.");
            }
            catch (ArgumentException ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private int ParseAndValidateInput(string input, int maxScore)
        {
            if (string.IsNullOrWhiteSpace(input))
            {
                throw new ArgumentException("Ошибка: необходимо ввести значение.");
            }

            if (!IsNumeric(input))
            {
                throw new FormatException("Ошибка: введено некорректное значение.");
            }

            int score = int.Parse(input);

            if (score > maxScore)
            {
                throw new ArgumentException($"Ошибка: введено значение, превышающее максимальное количество баллов ({maxScore}).");
            }

            return score;
        }

        private bool IsNumeric(string text)
        {
            return Regex.IsMatch(text, @"^\d+$");
        }

        private void StartTestButton_Click(object sender, RoutedEventArgs e)
        {
            Random random = new Random();
            Task1TextBox.Text = random.Next(12).ToString();
            Task2TextBox.Text = random.Next(52).ToString();
            Task3TextBox.Text = random.Next(32).ToString();
            Task4TextBox.Text = random.Next(12).ToString();

            // Вызов метода CalculateButton_Click для автоматического расчёта и вывода результата
            CalculateButton_Click(sender, e);
        }
    }
}
