for i in {1..5}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "PayBill_test_cases/PayBill_test_run_files/PayBill_Input_test_run/PayBill_${i}_INP.txt" "PayBill_${i}_OUT.txt"
done

echo "All test cases completed."
