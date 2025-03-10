for i in {1..6}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Transfer_test_cases/Transfer_test_run_files/Transfer_Input_test_run/Transfer_${i}_INP.txt" "Transfer_${i}_OUT.txt"
done

echo "All test cases completed."
