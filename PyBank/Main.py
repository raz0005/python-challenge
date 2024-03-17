import csv

# Function to analyze financial records
def analyze_financial_records(file_path):
    # Initialize variables to store financial analysis results
    total_months = 0
    net_total_profit_losses = 0
    profit_loss_changes = []
    previous_profit_loss = None
    greatest_increase = {"date": "", "amount": 0}
    greatest_decrease = {"date": "", "amount": 0}

    # Read the CSV file
    with open(file_path, newline="") as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)  # Skip header row

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Increment total months
            total_months += 1

            # Extract profit/loss amount from the row
            profit_loss = int(row[1])

            # Calculate net total profit/loss
            net_total_profit_losses += profit_loss

            # Track profit/loss changes and find greatest increase/decrease
            if previous_profit_loss is not None:
                change = profit_loss - previous_profit_loss
                profit_loss_changes.append(change)
                if change > greatest_increase["amount"]:
                    greatest_increase["date"] = row[0]
                    greatest_increase["amount"] = change
                elif change < greatest_decrease["amount"]:
                    greatest_decrease["date"] = row[0]
                    greatest_decrease["amount"] = change

            # Update previous profit/loss for the next iteration
            previous_profit_loss = profit_loss

    # Calculate average of profit/loss changes
    average_change = sum(profit_loss_changes) / len(profit_loss_changes)

    # Format the results
    analysis_results = {
        "Total Months": total_months,
        "Net Total Profit/Losses": net_total_profit_losses,
        "Average Change": average_change,
        "Greatest Increase in Profits": greatest_increase,
        "Greatest Decrease in Profits": greatest_decrease,
    }

    return analysis_results

# Function to write analysis results to a text file
def write_analysis_to_file(analysis_results):
    with open("financial_analysis.txt", "w") as txtfile:
        txtfile.write("Financial Analysis\n")
        txtfile.write("----------------------------\n")
        for key, value in analysis_results.items():
            if isinstance(value, dict):
                txtfile.write(f"{key}: {value['date']} (${value['amount']})\n")
            else:
                txtfile.write(f"{key}: {value}\n")
        txtfile.write("----------------------------\n")
    print("Analysis results have been written to financial_analysis.txt")

# Main function
def main():
    file_path = "Resources/budget_data.csv"
    analysis_results = analyze_financial_records(file_path)

    # Print the analysis results to the terminal
    print("Financial Analysis")
    print("----------------------------")
    for key, value in analysis_results.items():
        if isinstance(value, dict):
            print(f"{key}: {value['date']} (${value['amount']})")
        else:
            print(f"{key}: {value}")
    print("----------------------------")

    # Write the analysis results to a text file
    write_analysis_to_file(analysis_results)

if __name__ == "__main__":
    main()
