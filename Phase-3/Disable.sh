for i in {1..5}
do
    echo "Running test case $i..."
    python phase3_cmdlinearg.py "Disable_test_cases/Disable_test_run_files/Disable_Input_test_run/Disable_${i}_INP.txt" "Disable_${i}_OUT.txt"
done

echo "All test cases completed."
