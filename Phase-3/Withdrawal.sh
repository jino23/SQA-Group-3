for i in {1..4}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Withdrawal_test_cases/Withdrawal_test_run_files/Withdrawal_Input_test_run/Withdrawal_${i}_INP.txt" "Withdrawal_${i}_OUT.txt"
done

echo "All test cases completed."
