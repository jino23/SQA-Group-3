for i in {1..4}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Deposit_test_cases/Deposit_test_run_files/Deposit_Input_test_run/Deposit_${i}_INP.txt" "Deposit_${i}_OUT.txt"
done

echo "All test cases completed."
