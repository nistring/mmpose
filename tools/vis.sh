python ./tools/misc/browse_dataset.py configs/body_2d_keypoint/topdown_heatmap/gm/td-hm_ViTPose-base-simple_3xb128-210e-f0_gm-256x192.py --output-dir data/gm/gt_vis/train --not-show --phase train --mode original
python ./tools/misc/browse_dataset.py configs/body_2d_keypoint/topdown_heatmap/gm/td-hm_ViTPose-base-simple_3xb128-210e-f0_gm-256x192.py --output-dir data/gm/gt_vis/val --not-show --phase val --mode original
python ./tools/misc/browse_dataset.py configs/body_2d_keypoint/topdown_heatmap/gm/td-hm_ViTPose-base-simple_3xb128-210e-f0_gm-256x192.py --output-dir data/gm/gt_vis/test --not-show --phase test --mode original